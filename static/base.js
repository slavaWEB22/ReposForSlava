document.addEventListener("DOMContentLoaded", () => {
    let cloneNav;
    let observ = new ResizeObserver((arr) => {
        let header = document.querySelector("header")
        let baseContainer = document.querySelector(".base-container")
        let bottomPanel = document.createElement("div")
        for(let item of arr){
            let headerWidth = item.contentRect.width
            if(item.target.tagName == "HEADER" && headerWidth < 400){
                let nav = document.querySelector("nav")
                let cloneButtonLogin;
                let cloneButtonLogout;

                if(nav){
                    cloneNav = nav.cloneNode(true)
                    let cloneButtonHome = document.getElementById("btnHome")
                    cloneButtonHome.innerHTML = "<img src='/static/icons/bottomPanelIconHome.png' class='bottomPanelIcon'/>"
                        bottomPanel.append(cloneButtonHome)
                    if(nav.lastElementChild.textContent == "Вход"){
                        cloneButtonLogin = document.getElementById("btnLogin")
                        cloneButtonLogin.innerHTML = "<img src='/static/icons/bottomPanelIconLogin.png' class='bottomPanelIcon'/>"
                        
                        bottomPanel.append(cloneButtonLogin)
                    }else{
                        cloneButtonLogout = document.getElementById("btnLogout")
                        cloneButtonLogin.innerHTML = "<img src='/static/icons/bottomPanelIconLogin.png' class='bottomPanelIcon'/>"
                        bottomPanel.append(cloneButtonLogout)
                    }
                    nav.remove()
                    bottomPanel.classList.add("bottomPanel")
                    baseContainer.append(bottomPanel)
                }
            }else if(item.target.tagName == "HEADER" && headerWidth >= 400){
                if(!document.querySelector("nav")){
                    header.prepend(cloneNav)
                    let panel = document.querySelector(".bottomPanel")
                    panel.remove()
                }
            }
        }
    })

    let header = document.querySelector("header")

    if(header){
        observ.observe(header)
    }


})