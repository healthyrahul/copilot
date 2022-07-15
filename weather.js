let full_name = window.prompt("Please enter name?")

const first_character = full_name.charAt(0);
const last_character = full_name.charAt(full_name.length - 1);

if (first_character == last_character) {
    alert("“First and last character of the string are the same!")
}
else {
    alert("Nothing special!")
}
