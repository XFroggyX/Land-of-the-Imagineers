import * as THREE from './three.module.js'
import {THREEx} from './threex.domevents.js'
import {MapControls} from './OrbitControls.js'
import * as jQuery from './jquery-3.6.0.js'

const canvas = document.querySelector('.canvas');
const body = document.querySelector('body');

const renderer = new THREE.WebGLRenderer({antialias: true, canvas});

const scene = new THREE.Scene();
scene.background = new THREE.Color( 0xbfe3dd );

const EDGE_LEN = 20;

const width = canvas.clientWidth;
const height = canvas.clientHeight;

const camera = new THREE.PerspectiveCamera(60, 2, 0.1, 1000);
camera.position.set(EDGE_LEN / 2, 5, EDGE_LEN / 2)


const controls = new MapControls( camera, renderer.domElement );

controls.enableRotate = false
controls.enableZoom = false

controls.mouseButtons = {
	RIGHT: THREE.MOUSE.PAN
}

controls.panSpeed = 2

controls.minDistance = 5;
controls.maxDistance = 5;

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
      body.appendChild(createPopup());
      $('#createCity').modal('show');

      var button = document.getElementById("pop-but");
      var input = document.getElementById("pop-inp");

      var csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;


      button.onclick = function() {
        var val = input.value
        $.ajax({
        url: '/api/',
        method: 'post',
        dataType: 'json',
        data: {
            csrfmiddlewaretoken: document.querySelector('[name=csrfmiddlewaretoken]').value,
            name_town: val,
            point_x: cube.position.x,
            point_y: cube.position.z
        },
            success: function(data){
                cube.material.map = town_texture;
            }
        });
        $('#createCity').modal('hide');
        updateTowns();
      };
    }, false)

    return cube;
}


function createPopup(){
    var popup = document.createElement("div");
    popup.id = 'popup';

    popup.innerHTML = '' +
        '<div class="modal fade" style="width:660px;" id="createCity" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">' +
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


function updateTowns()
{
    $.ajax({
	url: '/api/',
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