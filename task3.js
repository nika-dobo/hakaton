// Task 3: Multiply Array Elements
// Instructions:
// Given an array [1, 2, 3, 4], use a loop to multiply all elements and store in product.

let arr = [1, 2, 3, 4];
let product = 1;
for (let i = 0; i < arr.length; i++) {
    product *= arr[i];
}
console.log(product);