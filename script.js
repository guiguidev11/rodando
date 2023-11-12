function toggleMode(){
  const html = document.documentElement
  html.classList.toggle('light')

  const img = document.querySelector("#profile img")

  if(html.classList.contains('light')){
    img.setAttribute('src', './assets/assets/avatar-light.png')
  } else{
    img.setAttribute("src", "./assets/assets/avatar.png")
  }
  // pegar a tag img
  
  // substituir a imagem
  // se tiver light mode adicionar a imagem light
  // se tiver sem light mode, manter a imagem normal
}


