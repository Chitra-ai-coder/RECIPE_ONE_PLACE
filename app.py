from flask import Flask, render_template, request, url_for
import pandas as pd
import re

app = Flask(__name__)

CSV_FILE = 'Cleaned_Indian_Food_Dataset.csv'
RECIPES_PER_PAGE = 48 

# These must match your CSV exactly. 
# If recipes aren't showing, it's usually because 'Indian' in the CSV 
# might be 'Indian Recipes' or have a space.
TARGET_CATEGORIES = [
    "Continental", "Indian", "North Indian Recipes", "South Indian Recipes",
    "Italian Recipes", "Maharashtrian Recipes", "Bengali Recipes", "Karnataka",
    "Tamil Nadu", "Kerala Recipes", "Fusion", "Mexican", "Andhra", 
    "Rajasthani", "Gujarati Recipes", "Goan Recipes", "Asian", 
    "Chettinad", "Thai", "Punjabi"
]

def load_and_clean_data():
    try:
        data = pd.read_csv(CSV_FILE)
        print(f"📊 CSV Loaded! Found {len(data)} total rows.")
        
        # --- SMART COLUMN DETECTOR ---
        cols = data.columns
        name_col = next((c for c in cols if 'Name' in c), cols[0])
        ing_col = next((c for c in cols if 'Ingredient' in c), cols[1])
        cuisine_col = next((c for c in cols if 'Cuisine' in c), cols[2])
        time_col = next((c for c in cols if 'Time' in c), cols[3])

        data = data.rename(columns={
            name_col: 'TranslatedRecipeName',
            ing_col: 'Cleaned-Ingredients',
            cuisine_col: 'Cuisine',
            time_col: 'TotalTimeInMins'
        })

        # Basic Cleaning
        data['TotalTimeInMins'] = pd.to_numeric(data['TotalTimeInMins'], errors='coerce').fillna(0).astype(int)
        data['Cuisine'] = data['Cuisine'].astype(str).str.strip()
        data['TranslatedRecipeName'] = data['TranslatedRecipeName'].astype(str).str.strip()
        
        # FILTER CHECK
        available_cuisines = data['Cuisine'].unique()
        print(f"🌍 Cuisines found in your CSV: {available_cuisines[:5]}...")
        
        # Keep only the ones we want
        filtered_data = data[data['Cuisine'].isin(TARGET_CATEGORIES)]
        print(f"✅ After filtering categories, {len(filtered_data)} recipes remain.")
        
        filtered_data.fillna('', inplace=True)
        return filtered_data
    except Exception as e:
        print(f"❌ CRITICAL ERROR: {e}")
        return pd.DataFrame()

df = load_and_clean_data()

@app.route('/')
def home():
    if df.empty:
        return "<h1>Database is Empty</h1><p>Check your terminal for the error message.</p>"

    selected_cuisine = request.args.get('cuisine', 'All')
    search_query = request.args.get('search', '').strip().lower()
    
    try:
        page = int(request.args.get('page', 1))
    except:
        page = 1
        
    filtered_df = df.copy()

    # --- STRICT SEARCH LOGIC ---
    if search_query:
        def get_strict_score(recipe_name):
            name = str(recipe_name).lower()
            clean_name = re.sub(r'[^\w\s]', ' ', name)
            # Match whole words only for 100% accuracy
            if re.search(r'\b' + re.escape(search_query) + r'\b', clean_name):
                return 100
            return 0

        filtered_df['score'] = filtered_df['TranslatedRecipeName'].apply(get_strict_score)
        filtered_df = filtered_df[filtered_df['score'] == 100]

    # Category Filter
    if selected_cuisine != 'All':
        filtered_df = filtered_df[filtered_df['Cuisine'] == selected_cuisine]

    # Pagination
    total_found = len(filtered_df)
    total_pages = max(1, (total_found + RECIPES_PER_PAGE - 1) // RECIPES_PER_PAGE)
    page = min(max(1, page), total_pages)
    
    start = (page - 1) * RECIPES_PER_PAGE
    recipes_to_show = filtered_df.iloc[start : start + RECIPES_PER_PAGE].to_dict(orient='records')

    return render_template('index.html', 
                           recipes=recipes_to_show, 
                           cuisines=TARGET_CATEGORIES, 
                           selected_cuisine=selected_cuisine,
                           total_found=total_found,
                           search_query=search_query,
                           current_page=page,
                           total_pages=total_pages)

@app.route('/recipe/<path:recipe_name>')
def recipe_detail(recipe_name):
    match = df[df['TranslatedRecipeName'] == recipe_name]
    if not match.empty:
        recipe_data = match.iloc[0].to_dict()
        # Clean ingredients/instructions for the detailed page
        ings = str(recipe_data.get('Cleaned-Ingredients', ''))
        recipe_data['ingredients_list'] = [i.strip() for i in ings.split(',') if i.strip()]
        inst = str(recipe_data.get('TranslatedInstructions', ''))
        recipe_data['instructions_list'] = [s.strip() + '.' for s in inst.split('.') if len(s.strip()) > 5]
        return render_template('recipe.html', recipe=recipe_data)
    return "Recipe not found", 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)