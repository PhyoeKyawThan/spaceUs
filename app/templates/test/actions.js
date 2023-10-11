export const isLove = (event) => {
    let loves = document.querySelectorAll("#love");
    loves.forEach(love => {
        love.addEventListener("click", (e) => {
            actions.push({
                "target": e.target.content,
                "id": e.target.id,
                "loved": true
            });
            event(true);
        });
    });
}

export const seeMore = (target, temp_caption, actual_caption)=> {
    target.addEventListener("click", (e)=>{
        temp_caption = actual_caption;
    });
    actual_caption.addEventListener("click", (e)=>{
        actual_caption = temp_caption;
    });
    return "See More";
}

// check data string is img dir or not
export let isImg = (str) => {
    const regPath = /\.(jpeg|jpg|png|gif)$/i;
    return regPath.test(str);
}