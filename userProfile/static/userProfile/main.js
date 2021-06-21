 var selected_tags=[];
 

 //var optional_tags = JSON.parse(json_optional_object)
 //console.log(optional_tags)
 const container = document.querySelector("#addedTags");
  function remove(element){
        element.remove()
    }

  function addtoArray(tag){   
      var text = document.createTextNode(tag.value)
      class_name = document.getElementById(tag.value).className
      if(class_name == "selected"){
            var child = document.getElementById("span_"+tag.value)
            child.remove()
            console.log("in list")
            //
            remove_fromArray(tag.value);
            document.getElementById(tag.value).className = "tags"
            
      }
      else{selected_tags.push(tag.value);
        var span = document.createElement('span');
         span.onclick = function (){

            var element = document.getElementById(this.innerHTML)
            element.className = "tags"
            this.parentElement.removeChild(this);  
            remove_fromArray(this.innerHTML)          
           }
        span.className = "span-slct"
        span.id = "span_"+tag.value
        container.appendChild(span)
        span.appendChild(text)
        document.getElementById(tag.value).className = "selected"
    }
  }
const custom_tag = document.getElementById("add-custom-tag")

custom_tag.addEventListener("click",function(){
  var element = document.getElementById("custom-tags")
  var text = document.createTextNode(element.value);
  if(element.value.trim().length<=0){
    return;
  }
  else{
    if(document.getElementById(element.value)){
        document.getElementById(element.value).click()
      }
    else if(!document.getElementById("span_"+element.value)){
           
        var span = document.createElement('span');
           span.onclick = function (){
               this.parentElement.removeChild(this);
               remove_fromArray(this.innerHTML)
           }
           span.className = "span-slct"
           span.id = "span_"+element.value
           container.appendChild(span)
           span.appendChild(text)
           selected_tags.push(element.value);
           element.value=""
          }      
  }
});

function remove_fromArray(text){
    index = selected_tags.indexOf(text)
    selected_tags.splice(index,1);
    let s = JSON.stringify(selected_tags)
    console.log(s.trim())
   }

document.getElementById("custom-tags").addEventListener("keyup",function(e){
  if(e.keyCode==13)
  {
    document.getElementById("add-custom-tag").click()
    document.getElementById("custom-tags").value = ""
    
  }
    
})

document.getElementById("next-btn").addEventListener("click",function(){
  let s = JSON.stringify(selected_tags)
  if(s.length<=2){
    alert("Please Select some tags to follow")
  }
  else{
   // const csrf = Cookies.get("csrftoken")
    let form = document.getElementById("interest")
    let input = document.createElement("input")
    input.setAttribute("type","hidden")
    input.setAttribute("name","tags")
    form.appendChild(input)
    input.value = s
    form.submit()
  }
})

function autocomplete(input)
{
  let counter = -1
  input.addEventListener("input",function(e){
    let hasVAl = false;
    if(input.value.length==0){
      remove_list(document.getElementById("suggestion-div"))
      return
    }
    remove_list(document.getElementById("suggestion-div"))
    val = input.value;
    div = document.createElement("DIV")
    div.setAttribute("id","suggestion-div")
    for(i=0;i<optional_tags.length;i++)
    {
        
      if(optional_tags[i].substr(0,val.length)==val){
          let b = document.createElement("DIV")
          b.innerHTML = "<strong>"+val+"</strong>"
          b.innerHTML += optional_tags[i].substr(val.length)
          b.setAttribute("class","suggestion")
          let text = optional_tags[i]
          b.addEventListener("click",function(e){
            input.value = text
            remove_list(document.getElementById("suggestion-div"))
            input.focus()
          })  
          div.appendChild(b);
          hasVAl=true;
        }
       
    }
      if(hasVAl===true){
      input.parentElement.appendChild(div)
    }
    else{
      div.remove()
    }
   
  })

  input.addEventListener("keydown",function(e){
      var suggestion_list = document.getElementById("suggestion-div")
      if(suggestion_list){
        suggestion_list = suggestion_list.getElementsByTagName("div")
        if(e.keyCode == 40)
        {
          // Down arrow
          counter++;
          makeActive(suggestion_list);
        }
        else if(e.keyCode==38)
        {
          // Up arrow
          counter--;
          makeActive(suggestion_list);
        }
      }
  })
function makeActive(list){
    if(counter>=list.length) counter = 0;
    if(counter<0) counter = list.length-1; 
    makeUnactive(list)
    list[counter].classList.add("active");
    input.value = list[counter].textContent
  }
function makeUnactive(list){
  for(i=0;i<list.length;i++)
  {
    list[i].classList.remove("active")
  }
}
function remove_list(element)
  {
    if(element != undefined){
      element.parentElement.removeChild(element)
    } 
    counter=-1
  }
}





autocomplete(document.getElementById("custom-tags"));
  