import {createApp,ref} from 'vue'

var Season_menu_btn = document.getElementById("Season_menu_btn");
var Lenten_menu_btn = document.getElementById("Lenten_menu_btn");
var Mushroom_menu_btn = document.getElementById("Mushrooms_menu_btn");
var NewYear_menu_btn = document.getElementById("NewYear_menu_btn");
var Maslentsa_menu_btn = document.getElementById("Maslenitsa_menu_btn");
var Main_menu_btn = document.getElementById("Main_menu_btn");
var Bar_menu_btn = document.getElementById("Maslenitsa_menu_btn");
var Wine_menu_btn = document.getElementById("Maslenitsa_menu_btn");
let response;
const apiurl = "https://menuCB/api/"
Season_menu_btn.addEventListener('click', async () =>{
 const xhr = new XMLHttpRequest();
  xhr.open('GET', apiurl + "Get_menu", true);
   xhr.onload = function() {
        if (this.status === 200) {
            const items = JSON.parse(this.responseText);
            let output = '';
            items.forEach(function(item) {
                output+= '<div> <img src=item.img> '


            }
})

