const API_KEY = "75e3c060122946e59f1a5c5c6782ca01";

async function getRecipes(fruits) {
  const response = await fetch(`https://api.spoonacular.com/recipes/complexSearch?query=${fruits.join(',')}&apiKey=${API_KEY}`);
  const data = await response.json();
  return data.results;
}

const dummyFruits = ["apple", "banana"];

getRecipes(dummyFruits).then(recipes => {
  recipes.forEach(recipe => {
    console.log(`ID: ${recipe.id}`);
    console.log(`Title: ${recipe.title}`);
    console.log(`Image: ${recipe.image}`);
  });
});