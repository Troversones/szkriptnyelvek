let o1 = {};
let o2 = new Object();
let o3 = {
    nev: "Bence",
    kor: 25,
    szak: "Bprof"
};

console.log(o3);
console.log(o3.nev);
console.log(o3["nev"]);

o3.test = "test";
console.log(o3);
delete o3.test;
console.log(o3);

let human1 = {
    name: "Test1",
    age: 20,
    address: {
        city: "Test city",
        zipCode: "Test street 1."
    }
}

let human2 = {
    name: "Test2",
    age: 25
}

console.log(human1.address?.city ?? "Nincs");
console.log(human2.address?.city ?? "Nincs");
console.log("-------");

if("asdsgfd" in human1){
    console.log("Van");
}else{
    console.log("Nincs");
}
console.log("-------");
console.log("Object bejárási módszerek.")

for(let i in human2){
    console.log(`${i} -> ${human2[i]}`);
}
console.log("-------");

for(let i of Object.keys(human1)){
    console.log(`${i} -> ${human2[i]}`);
}
console.log("-------");

for(let i of Object.values(human2)){
    console.log(`ertek: ${i}`);
}
console.log("-------");

for(let [k,v] of Object.entries(human2)){
    console.log(`${k} -> ${v}`);
}
console.log("-------");
console.log("Érték befagyasztás - Freeze");

Object.freeze(human1);
human1.name = "ChangeWhileFreezed"; // Nincs változás bármilyen meglepő
human1.testkey = "testkey"; //új kulcs se megy hozzá
human1.address.city = "testChange"; // ez egy nestelt object eleme amit már tudunk változtatni mert nem a main objectre vonatkozik amire kiadtam a freeze-t
delete human1.name;
console.log(human1);
console.log("-------");
console.log("Json formázások");

let jsonString = JSON.stringify(human1, null, 2);
console.log(jsonString);

let json = JSON.parse(jsonString);
console.log(json);
//nem lehet összehasonlítani === -vel
console.log("--------");
let h = {
    ...human1,
    ...human2
}

console.log(human1);
console.log(human2);
console.log(h);