let str_name = prompt("Enter the Name");

let forbiddenChar = " =?*^$№@".split("")
let isForbiddenPresent = false;
for(let i = 0; i < forbiddenChar.length; i++)
{
    if(str_name.includes(forbiddenChar[i]))
    {
        alert(`This symbol [${forbiddenChar[i]}] is forbidden.`)
        isForbiddenPresent = true;
        break;
    }
}
if(!isForbiddenPresent)
{
    alert("Correct");
}