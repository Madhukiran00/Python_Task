// const url = "http://127.0.0.1:8000/mydetails/";
// fetch(url)
//   .then(response => response.json())
//   .then(data => {
//     const container = document.getElementById("mydetails");

//     // Insert the fetched data into the HTML
//     container.innerHTML = `
//       <h2>My Details</h2>
//       <p><strong>Name:</strong> ${data.NAME}</p>
//       <p><strong>Mobile:</strong> ${data.MOB}</p>
//       <p><strong>Email:</strong> ${data.EMAIL}</p>
//     `;
//   })

key="79ff9b2dc48b43dbacf0226fe60c216b"

fetch("https://newsapi.org/").then(response => response.json()).then(data=>console.log(data))




