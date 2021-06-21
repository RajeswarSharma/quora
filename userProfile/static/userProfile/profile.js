function activate(element,index){
    let parent = element.parentElement
    let child = parent.getElementsByClassName("inner-tab")
    for(i =0 ; i < child.length;i++){
        child[i].classList.remove("active")   
    }
    element.classList.add("active")
    let details = document.getElementsByClassName("details")

    for(i=0;i<details.length;i++){
        details[i].style.display = "none"
    }
    details[index].style.display="block"
}

