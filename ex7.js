console.log("ex7")

fetch( 'https://reqres.in/').then(response => response.json())
.then(responseJSON => create_user_list(responseJSON.data)).catch(err => console.log(err));

function create_user_list(users){
    console.log(users);
    const curr_main = document.querySelector("main");
    for (let user of users){
        const selection = document.createElement("selection");
        selection.innerHTML = <div></div>;
        curr_main.appendChild(selection);
    }

}