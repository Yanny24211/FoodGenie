async function getRecipe()
{
    const response = await fetch(`https://api.spoonacular.com/recipes/findByIngredients?apiKey=75e3c060122946e59f1a5c5c6782ca01&ingredients=${apple}&number=10&ignorePantry=true`)
    const recipeSlip = await response.json();
} 