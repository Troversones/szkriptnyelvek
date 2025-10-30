console.log(Math.PI);
console.log(Math.round(5.6)); //default kerekítés
console.log(Math.floor(5.6)); //felfele kerekítés
console.log(Math.ceil(5.1)); //lefele kerekítés
console.log(Math.sqrt(25)); //square root xd
console.log(Math.pow(25,3)); //25 on the pow(er) of 3 if you catch my drift 25^3
console.log(Math.asin(1)); 
console.log(Math.floor(Math.random()*10+1)); //1-10 közötti szám
console.log("---------------");

console.log("First");

setTimeout(() => {
    console.log("szopj le");
}, 12000);

const promise = new Promise((resolve, reject) => {
    const randomNumber = Math.random();

    if(randomNumber > 0.5){
        resolve(`Success! Number: ${randomNumber}`);
    }else{
        reject(`Error! Number too small: ${randomNumber}`);
    }
});

promise
    .then(result => {
        console.log("Successful operation:", result);
    })
    .catch(error => {
        console.log("Error occurred:", error);
    })
    .finally(() => {
        console.log("Az konkrét");
    });

