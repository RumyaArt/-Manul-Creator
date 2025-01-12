class Item {
    constructor() {
        this.show =   false;
        this.name =   null;
        this.base =   null;
        this.stroke = null;
        this.adds =   [];
    }


    getImages(node)
    {
        //console.log(node)
        if ('name' in node)
            this.name = node['name'];

        this.base = new Image;
        this.base.src = node['base'];

        if ('stroke' in node)
        {
            this.stroke = new Image;
            this.stroke.src = node['stroke']
        }
        
        for (let value = 1; ;value++)
            if (parseInt(value) in node)
            {
                //console.log(value);
                this.adds[value] = new Image;
                this.adds[value].src = node[value];
            }
            else
                break
    }
}

var Hats      = []
var EyesAcc   = []
var EyesEmo   = []
var HairSyles = []
var Mouth     = []
var Neck      = []
var Body      = []
var RightHand = []
var LeftHand  = []
var Tops      = []
var Bottoms   = []
var Lingeries = []
var Dresses   = []


function buildStructures()
{
    return fetch('data.json')
        .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json(); // Преобразование ответа в JSON
        })
        .then(data => {
            console.log('JSON data:', data); // Обработка JSON данных

            function build(array, name)
            {
                for(let value in data[name]){
                    array.push(new Item());
                    array[parseInt(value - 1)].getImages(data[name][value]);
                    //console.log(array[parseInt(value - 1)])
                }
            }

            build(Hats, 'HATS');                 
            build(EyesAcc, 'EYES_ACCESSORIES');   
            build(EyesEmo, 'EYES_EMOTIONS');      
            build(Mouth, 'MOUTH')                 
            build(HairSyles, 'HAIRSTYLES');       
            build(Neck, 'NECK');                  
            build(Body, 'BODY');                  
            build(RightHand, 'RIGHT_HAND');       
            build(LeftHand, 'LEFT_HAND');         
            build(Tops, 'TOPS');                 
            build(Bottoms, 'BOTTOMS');            
            build(Lingeries, 'LINGERIES');        
            build(Dresses, 'DRESSES');  

            return true;
        })
        .catch(error => {
            console.error('Ошибка при обработке JSON:', error);
        });

}


function draw(element, node)
{
    console.log(node.name)
    console.log(node)
    console.log(element)
    let layers = element.getElementsByClassName('layer');
    console.log(layers);
    let contexts = []
    for (let value = 0; value < layers.length; value++)
        contexts[value] = layers[value].getContext('2d');
        
    if(node.base)
        contexts[0].drawImage(node.base, 0,0);

    if(node.stroke)
        contexts[6].drawImage(node.stroke, 0,0);

    for (value in contexts)
        if(node.adds[value])
            contexts[value].drawImage(node.adds[value], 0,0);
    
}


async function test()
{
    await buildStructures();

    canvases = document.getElementsByClassName('layer');
    for (canvas of canvases)
    {
        canvas.width = 480;
        canvas.height = 480;
    }

    body = document.getElementById('mbody');
    eyes = document.getElementById('eyes-emo');
    mouth = document.getElementById('mouth');
    mtop = document.getElementById('mtop');
    mbottom = document.getElementById('mbottom');
    hat = document.getElementById('hat');
    eyesacc = document.getElementById('eyes-acc');
    rightHand = document.getElementById('right-hand');
    leftHand = document.getElementById('left-hand');


    draw(body, Body[1])
    draw(mouth, Mouth[2])
    draw(eyes, EyesEmo[0])
    draw(mtop, Tops[4])
    draw(mbottom, Bottoms[3])
    draw(hat, Hats[4])
    draw(eyesacc, EyesAcc[3])
    draw(rightHand, RightHand[13])
    draw(leftHand, LeftHand[2])
    
}



test();