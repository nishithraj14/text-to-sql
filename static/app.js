async function ask() {
    const q = document.getElementById("question").value;
    const output = document.getElementById("output");
  
    output.textContent = "Running query...";
  
    try {
      const res = await fetch("/query", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: q })
      });
  
      const data = await res.json();
  
      output.textContent =
        "Generated SQL:\n" + data.sql +
        "\n\nResult:\n" + JSON.stringify(data.result, null, 2);
  
    } catch (err) {
      output.textContent = "Error: " + err.message;
    }
  }
  