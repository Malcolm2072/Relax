const container  = document.getElementById('container');
const text = document.getElementById('text');


const totaltime = 7500;
const breathetime = (totaltime / 5) * 2 ;
const holdtime = totaltime / 5; 


var music = "{% static 'audio\music.mp3' %}";
var bgaudio = new Audio();
var breathein = document.getElementById("breathein");
var hold = document.getElementById("hold");
var breatheout = document.getElementById("breatheout");


bgaudio.src = music;

bgaudio.volume = 0.15;
bgaudio.autoplay = true;

breatheanimation();

function breatheanimation()
{
    text.innerText = 'Breathe in';
    container.className = 'container grow'; 
    breathein.play();

    setTimeout(() => {
        text.innerText = 'Hold';
        hold.play();

        setTimeout(() => {
            text.innerText = 'Breath Out';
            container.className = 'container shrink';
            breatheout.play();
        },holdtime);
    },breathetime);


}

setInterval(breatheanimation, totaltime);