import * as THREE from './three.module.js'
import {THREEx} from './threex.domevents.js'
import {MapControls} from './OrbitControls.js'
import * as jQuery from './jquery-3.6.0.js'
import {GLTFLoader} from './GLTFLoader.js'

const canvas = document.querySelector('.canvas');
const body = document.querySelector('body');

const renderer = new THREE.WebGLRenderer({antialias: true, canvas});

const scene = new THREE.Scene();
scene.background = new THREE.Color( 0xc0c0c0 );

const EDGE_LEN = 20;

const width = canvas.clientWidth;
const height = canvas.clientHeight;

const camera = new THREE.PerspectiveCamera(60, 2, 0.1, 1000);
camera.position.set(EDGE_LEN / 2, 5, EDGE_LEN / 2);



const controls = new MapControls( camera, renderer.domElement );

controls.enableRotate = false
controls.enableZoom = false

controls.mouseButtons = {
	RIGHT: THREE.MOUSE.PAN
}

controls.panSpeed = 2

controls.minDistance = 5;
controls.maxDistance = 5;

controls.minPolarAngle = 0.79; // radians
controls.maxPolarAngle = 0.79; // radians


const light = new THREE.DirectionalLight(0xffffff, 1);
light.position.set(0, 10, 0)

let domEvents = new THREEx.DomEvents(camera, renderer.domElement);
const geometry = new THREE.PlaneGeometry();

const town_texture = new THREE.TextureLoader().load('../../static/img/textures/town.png');
town_texture.magFilter = THREE.NearestFilter;

const texture = new THREE.TextureLoader().load('../../static/img/textures/grass(no).png');
texture.magFilter = THREE.NearestFilter;


let cubes = [];
for(let i = 0; i < EDGE_LEN; i++)
{
    cubes.push([]);
    for(let j = 0; j < EDGE_LEN; j++)
    {
        cubes[i].push(makeInstance(geometry, i, 0, j));
    }

}


$(document).on('hidden.bs.modal','#createCity', function (){
    var child = document.getElementById("popup");
    body.removeChild(child);
});

updateTowns();

let id = 0;
let username = "";
$.ajax({
	url: '/api/current_user/',
	method: 'get',
	async: false,
	dataType: 'json',
	success: function(data){
            id = data.id;
            username = data.username;
            console.log(data);
    }
});

var townsID = null;
$.ajax({
	url: '/api/user_list/',
	method: 'get',
	dataType: 'json',
	success: function(data){
	    console.log(data);
        for(let i = 0; i < data.length; ++i) {
            if(data[i].UsersID == id){
               townsID = data[i].TownsID;
               break;
            }
            townsID = null;
        }
        alert(townsID);
    }
});



$.ajax({
	url: '/api/battle/' + id +  '/get_result_battle/',
	method: 'get',
	dataType: 'json',
	success: function(data){
        if(data[0].result == id)
        {
           body.appendChild(createVictoryPopup());
           $('#attackWin').modal('show');
        } else {
           body.appendChild(createLosePopup());
           $('#attackLose').modal('show');
        }
    }
});



function render() {
    if (resizeRendererToDisplaySize(renderer)) {
        const canvas = renderer.domElement;
        camera.aspect = canvas.clientWidth / canvas.clientHeight;
        camera.updateProjectionMatrix();
    }
    renderer.render(scene, camera);

    requestAnimationFrame(render);
}


function resizeRendererToDisplaySize(renderer) {
    const canvas = renderer.domElement;
    const width = canvas.clientWidth;
    const height = canvas.clientHeight;
    const needResize = canvas.width !== width || canvas.height !== height;
    if (needResize) {
        renderer.setSize(width, height, false);
    }
    return needResize;
}


function makeInstance(geometry, x, y, z) {
    const material = new THREE.MeshBasicMaterial({
        map: texture,
    });

    const cube = new THREE.Mesh(geometry, material);

    scene.add(cube)

    cube.position.x = x;
    cube.position.y = y;
    cube.position.z = z;

    cube.rotation.x = -1.5708;


    domEvents.addEventListener(cube, 'click', function(event){
        var flag = false;
        var clickUserId;
        var clickTownsId;
        $.ajax({
        url: '/api/town/',
        method: 'get',
        async : false,
        dataType: 'json',
        success: function(data){
            for (let index = 0; index < data.length; ++index) {
                if (data[index].point_x == cube.position.x && data[index].point_y == cube.position.z)
                {
                    flag = true;
                    clickTownsId = data[index].id;


                    $.ajax({
                        url: '/api/user_list/',
                        method: 'get',
                        dataType: 'json',
                        async: false,
                        success: function(data){
                            for(let i = 0; i < data.length; ++i) {
                                if(data[i].TownsID == clickTownsId){
                                   clickUserId = data[i].UsersID;
                                   break;
                                }
                            }
                            console.log(data);
                        }
                    });

                    break;
                }
            }
        }
        });

      if(townsID == null && flag == 0) {

      body.appendChild(createPopup());
      $('#createCity').modal('show');

      var button = document.getElementById("pop-but");
      var input = document.getElementById("pop-inp");

      updateTowns();
      button.onclick = function() {
        var val = input.value
        $.ajax({
        url: '/api/town/',
        method: 'post',
        dataType: 'json',
        data: {
            csrfmiddlewaretoken: document.querySelector('[name=csrfmiddlewaretoken]').value,
            name_town: val,
            point_x: cube.position.x,
            point_y: cube.position.z,
            stone: 100,
            wood: 100,
            iron: 100
        },
            success: function(data){
                console.log(data);
                setTowns();
                updateTowns();
            }
        });
        $('#createCity').modal('hide');
      };
    }
      else if (townsID != null && flag == 1) {
      body.appendChild(createAttackPopup());
      $('#attackCity').modal('show');

      var button = document.getElementById("pop-but");

      updateTowns();
      button.onclick = function() {

        $.ajax({
        url: '/api/battle/start_battle/',
        method: 'post',
        dataType: 'json',
        data: {
            csrfmiddlewaretoken: document.querySelector('[name=csrfmiddlewaretoken]').value,
            attacking: id,
            defending: clickUserId
        },
            success: function(data){
                updateTowns();
            }
        });

        $('#attackCity').modal('hide');
      };

    }
    }, false)

    return cube;
}





function createPopup(){
    var popup = document.createElement("div");
    popup.id = 'popup';

    popup.innerHTML = '' +
        '<div class="modal fade" id="createCity" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">' +
            '<div class="modal-dialog">' +
                '<div class="modal-content">' +
                    '<div class="modal-body container">' +
                        '<div class="popup-input element">' +
                            '<input id="pop-inp" class="in-input pb-3" type="text"  placeholder="Название города">' +
                        '</div>' +
                        '<div class="popup-button element">' +
                            '<button id="pop-but" class="in-button"></button>' +
                        '</div>' +
                    '</div>' +
                 '</div>' +
            '</div>' +
            '</div>' +
        '</div>';

    return popup;
}


function createAttackPopup(){
    var popup = document.createElement("div");
    popup.id = 'popup';

    popup.innerHTML = '' +
    '<div class="modal fade" id="attackCity" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">'+
    '<div class="modal-dialog">'+
        '<div class="modal-content">'+
                '<div class="modal-body container">'+
                    '<div class="popup-label element">'+
                        '<label>%cityname%</label>'+
                    '</div>'+
                    '<div class="popup-button-attack element">'+
                        '<button id="pop-but" class="in-button"></button>+'
                        '</div>'+
                   ' </div>'+
                '</div>'+
        '</div>'+
    '</div>'+
'</div>';

    return popup;
}


function createLosePopup(){
    var popup = document.createElement("div");
    popup.id = 'popup';

    popup.innerHTML = '' +
    '<div class="modal fade" id="attackLose" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">'+
    '<div class="modal-dialog">'+
        '<div class="modal-content-lose">'+
            '<div class="element">'+
                '<input class="in-input pb-3" type="text">'+
            '</div>'+
        '</div>'+
    '</div>'+
'</div>';

    return popup;
}


function createVictoryPopup(){
    var popup = document.createElement("div");
    popup.id = 'popup';
    popup.innerHTML = '' +
    '<div class="modal fade" id="attackWin" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">'+
    '<div class="modal-dialog">'+
        '<div class="modal-content-win">'+
                '<div class="modal-body container">'+
                    '<div class="element">'+
                        '<input class="in-input pb-3" type="text">'+
                    '</div>'+
                '</div>'+
        '</div>'+
    '</div>'+
'</div>';

    return popup;
}




function setTowns()
{
    $.ajax({
	url: '/api/town/',
	method: 'get',
	dataType: 'json',
	success: function(data){
        $.ajax({
        url: 'http://127.0.0.1:8000/api/user_list/1/edit_user_town/',
        method: 'post',
        dataType: 'json',
        data: {
            csrfmiddlewaretoken: document.querySelector('[name=csrfmiddlewaretoken]').value,
            UsersID: id,
            TownsID: data[Object.keys(data).length - 1].id
        }
        });

    }
    });
}


function updateTowns()
{
    $.ajax({
	url: '/api/town/',
	method: 'get',
	dataType: 'json',
	success: function(data){
        for (let index = 0; index < data.length; ++index) {
            cubes[data[index].point_x][data[index].point_y].material.map = town_texture;
        }
    }
    });
}


requestAnimationFrame(render);