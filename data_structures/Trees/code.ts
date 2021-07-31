const student_data = [
  {
    name: "joe",
    age: 17,
  },
  {
    name: "joe",
    age: 13,
  },
  {
    name: "swayam",
    age: "??",
  },
];

function checkObj(obj: any) {
  return student_data.some((entry) => entry.name == obj.name && entry.age == obj.age);
}

console.log(checkObj({ name: "joe", age: 32 }));

let arr = [1,2,3,4]
let clone = [1,2,3,4]

console.log(arr.every((int , idx) => int == clone[idx]))
console.log(arr.entries())



