class Phone {
    #type; // private típus
    static NOP = 0;


    constructor(brand, type){ //default értéket lehet adni = "valami"
        this._brand = brand;
        this.#type = type;
        this.apps = [];
        Phone.NOP++; // statikus érték meghívása a classra és ez az egész classra vonatkozóan számol egy értéket hogy mennyi telefon lett készítve
    }

    static numberOfPhones(){
        return `${Phone.NOP} phone(s) were made.`; //statikus metódus a statikus adattaggal
    }

    get type(){ // ezzel lehet hívni private tagot
        return this.#type;
    }

    set type(newParam){
        this.#type = newParam;
    }

    info(){
        console.log(`The phone's brand is ${this._brand}, type: ${this.type} and we have ${this.apps.length} apps avaliable`);
    }

    addApps(app){
        if(typeof app === 'string'){
            this.apps.push(app);
        }
    }
}

class SmartPhone extends Phone{
    constructor(brand, type){
        super(brand, type); // ősosztály konstruktor
        this.wifi = true; 
    }

    info(){
        super.info(); // ősosztály metódus meghívása
        console.log(`The wifi is currently ${this.wifi ? "turned on" : "turned off"} on this phone.`);
    }
}

let t1 = new Phone("Xiaomi", "14T");
let o1 = new SmartPhone("Samsung", "Galaxy s6");
console.log(t1._brand);
//console.log(t1.#type); private nem lehet elérni
t1.type = "14T Pro";
console.log(t1.type);
t1.info();
t1.addApps("Messenger");
t1.addApps(67); // nem megy át mert van type check
t1.info();

console.log(Phone.numberOfPhones()); // statikus metódus hívás az osztályra
o1.info(); // okostelefon felülírt info metódusa

