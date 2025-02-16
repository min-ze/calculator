async function calculate(operation) {
    let num1 = document.getElementById('num1').value || 0;
    let num2 = document.getElementById('num2').value || 0;

    let formData = new URLSearchParams();
    formData.append("num1", num1);
    formData.append("num2", num2);

    let response = await fetch(`http://127.0.0.1:5000/${operation}`, {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: formData
    });

    if (!response.ok) {
        document.getElementById("result").innerText = "Error!";
        return;
    }

    let data = await response.json();
    document.getElementById("result").innerText = data.result;
}
