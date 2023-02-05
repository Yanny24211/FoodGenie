const fileInput = document.getElementById("fileInput");
const processButton = document.getElementById("processButton");
const imageContainer = document.getElementById("image-box");
const grid = document.getElementById("grid-container"); 



processButton.addEventListener('click', function(){
  //alert("button clicked")
  for(let i = 0; i < 4; i++){
    const file = fileInput.files[i];
    const reader = new FileReader(); 
    let divR = document.createElement('div'); 
    divR.classList.add("recipe-grid");
    reader.onload = function () {
      divR.innerHTML = `<img src="${reader.result}" style="max-width: 100%; max-height: 100%; "  />`;
    };
    reader.readAsDataURL(file); 
    grid.appendChild(divR); 
  }
});
  
fileInput.addEventListener('change', function(){
  let divs = document.querySelectorAll(".recipe-grid"); 
  for(let div of divs){
    div.remove(); 
  }
});