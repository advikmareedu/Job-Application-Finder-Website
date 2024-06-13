const myForm = document.getElementById("buttons");
const inpFile = document.getElementById("fileUpload");

myForm.addEventListener("submit", e => {
    e.preventDefault(); // Prevent the form from submitting the traditional way

    const endpoint = "http://localhost:8000/upload.php";
    const formData = new FormData();

    formData.append("inpFile", inpFile.files[0]);

    fetch(endpoint, {
        method: "post",
        body: formData
    })
    
});

function updateJobLinks() {
    fetch('links.json') // Fetch the job links file
        .then(response => response.json())
        .then(jobLinks => {
            let tableBody = document.querySelector("#jobLinksTable tbody");
            tableBody.innerHTML = ""; // Clear existing rows
            jobLinks.forEach(link => {
                let row = document.createElement("tr");
                //let websiteCell = document.createElement("td");
                let linkCell = document.createElement("td");
                let anchor = document.createElement("a");
                anchor.href = link;
                anchor.textContent = link;
                linkCell.appendChild(anchor);
                //row.appendChild(websiteCell);
                row.appendChild(linkCell);
                tableBody.appendChild(row);
            });
        })
        .catch(error => {
            console.error('Error fetching job links:', error);
        });

    
}

// Update job links every 2 seconds (adjust as needed)

setInterval(updateJobLinks, 2000);
