import { isImg, seeMore } from "./actions.js";
export let post = (datas, activity) => {
    // create div

    let divs = {
        "post": null,
        "profile": null,
        "img": null,
        "name": null,
        "caption": null,
        "pic": null,
        "post_img": null,
    }
    for (let key in divs) {
        if (key === "img" || key === "post_img") {
            divs[key] = document.createElement("img");
        } else {
            divs[key] = document.createElement("div");
            divs[key].className = key;
        }
    }
    // add each child to relate parent

    divs["profile"].appendChild(divs["img"]);
    divs["post"].appendChild(divs["profile"]);
    divs["post"].appendChild(divs["name"]);
    divs["post"].appendChild(divs["caption"]);
    divs["post"].appendChild(divs["pic"]);
    divs["pic"].appendChild(divs["post_img"]);
    // divs["post"].appendChild(divs["activity"]);
    divs["post"].appendChild(activity);

    for (let data in datas) {
        if (isImg(datas[data])) {

            if (data === "img") {
                // console.log(datas[data]);
                divs["img"].src = datas[data];
            } else {
                // console.log(datas[data]);
                divs["post_img"].src = datas[data];
            }

        }else if(data === "caption"){
            let temp_caption = document.createElement("span");
            temp_caption.className = "caption";
            temp_caption.innerHTML = datas[data].substring(0, 100);
            let seemore = document.createElement("span");
            seemore.className = "seemore";
            let actual_caption = document.createElement("span");
            actual_caption.innerHTML = datas[data];
            if(datas[data].length > 100){
                divs[data].textContent =  `${temp_caption.textContent} ${seeMore(seemore, temp_caption, actual_caption)}`;
            }else{
                divs[data].textContent = datas[data];
            }
        }else if(data === "name"){
            divs[data].textContent = data[data];
        }
    }
    // console.log(temp_caption);
    return divs["post"];
}
