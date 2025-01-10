class Item {
    constructor() {
        this.name =   null;
        this.base =   null;
        this.stroke = null;
        this.adds =   [];
    }


    getImages(node)
    {
        console.log(node)
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
                console.log(value);
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
var Neck      = []
var Body      = []
var RightHand = []
var LeftHand  = []
var Tops      = []
var Bottoms   = []
var Lingeries = []
var Dresses   = []


var canvas = document.getElementById("window"),
    ctx     = canvas.getContext('2d');
    ctx.fillStyle = "white";
    ctx.fillRect(0, 0, canvas.width, canvas.height);


 fetch('data.json')
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
            }
        }

        build(Hats, 'HATS');
        build(EyesAcc, 'EYES_ACCESSORIES');
        build(EyesEmo, 'EYES_EMOTIONS');
        build(HairSyles, 'HAIRSTYLES');
        build(Neck, 'NECK');
        build(Body, 'BODY');
        build(RightHand, 'RIGHT_HAND');
        build(LeftHand, 'LEFT_HAND');
        build(Tops, 'TOPS');
        build(Bottoms, 'BOTTOMS');
        build(Lingeries, 'LINGERIES');
        build(Dresses, 'DRESSES');

        
    })
    .catch(error => {
        console.error('Ошибка при обработке JSON:', error);
    });