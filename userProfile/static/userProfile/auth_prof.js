function clicked(){
    var bio = document.getElementById("bio-txt")
    bio.setAttribute("contentEditable","true")
    var edt_btn = document.getElementsByClassName("edt-b")[0]
    var parent = edt_btn.parentElement
    parent.removeChild(edt_btn)
    var div = document.getElementById("sv-wrapper")
    div.setAttribute("id","sv-wrapper")
    
    var save_btn = document.createElement("btn")
    save_btn.setAttribute("type","submit")
    save_btn.setAttribute("form","bio-frm")
    save_btn.classList.add('edt-b')
    save_btn.innerHTML="Save"
    save_btn.addEventListener('click',function(e){
        var input = document.createElement("input")
        var form = document.getElementById("bio-frm")
        input.setAttribute("name","new-bio-tt")
        input.setAttribute("type","hidden")
        form.appendChild(input)
        input.value = document.getElementById("bio-txt").innerHTML
        form.submit()   
    })
    div.appendChild(save_btn)
    
    var cancel_btn = document.createElement("btn")
    cancel_btn.classList.add('edt-b')
    cancel_btn.innerHTML="Cancel"
    cancel_btn.style.backgroundColor="rgb(185"+","+"43"+","+"39)" //rgb(185,43,39)
    cancel_btn.addEventListener("click",function(e){
        bio.removeAttribute("contentEditable")
        cancel_btn.remove()
        save_btn.remove()
        div.appendChild(edt_btn)
       
    })
    div.appendChild(cancel_btn)
    bio.focus()
}