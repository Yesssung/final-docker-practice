document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("incrementButton").addEventListener("click", async function() {
        try {
            // 서버에 count 업데이트 요청
            const response = await fetch("http://localhost:8000/increment", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
            });

            if (!response.ok) {
                throw new Error("Network response was not ok");
            }

            // 서버에서 count 가져오기
            const response2 = await fetch("http://localhost:8000/count", {
                method: "GET",
                headers: {
                    "Content-Type": "application/json"
                },
            });

            const data = await response2.json();

           document.getElementById("result").textContent = data.count;

        } catch (error) {
            console.error("Failed to update count:", error);
        }
    });

    document.getElementById("decrementButton").addEventListener("click", async function() {
        try {
            // 서버에 count 업데이트 요청
            const response = await fetch("http://localhost:8000/decrement", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
            });

            if (!response.ok) {
                throw new Error("Network response was not ok");
            }

            // 서버에서 count 가져오기
            const response2 = await fetch("http://localhost:8000/count", {
                method: "GET",
                headers: {
                    "Content-Type": "application/json"
                },
            });

            const data = await response2.json();

             document.getElementById("result").textContent = data.count;
        } catch (error) {
            console.error("Failed to update count:", error);
        }
    });
});
