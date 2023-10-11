import { isLove, seeMore } from "./actions.js";
import { post } from "./post.js";
// test data
const datas = {
    "img": "./wallpaperflare.com_wallpaper.jpg",
    "name": "Dom AK",
    "caption": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quibusdam cum reprehenderit consequuntur porro impedit eveniet atque voluptatum nihil voluptate accusantium quia, fugiat excepturi iusto sint tempora sequi mollitia blanditiis tenetur.",
    "post_img": "./coffee.jpeg"
}


export let actions = []
// post template



// main method
const main = () => {
    const container = document.querySelector(".container");
    let data_container = document.querySelector(".data-container");
    let post_area = document.querySelector(".post-area");

    for (let i = 0; i < 10; i++) {
        let activity = document.createElement("div");
        activity.className = 'activity';
        let love = document.createElement("div");
        let interested = document.createElement("div");
        let save = document.createElement("div");
        
        // set id and class
        love.id = "love";
        love.textContent = "Love";
        interested.id = "interested";
        interested.textContent = "Interested";
        save.id = "save";
        save.textContent = "Save";

        love.content = `love ${i}`;
        interested.content =  `Interested ${i}`;
        save.content = `save ${i}`;

        activity.appendChild(love);
        activity.appendChild(interested);
        activity.appendChild(save);
        post_area.appendChild(post(datas, activity));
    }

    container.appendChild(data_container);
    data_container.appendChild(post_area);
    // action
    isLove((click)=>{
        if(click){
            alert(actions[0].target);
            actions.length = 0;
        }
    });
}

main();