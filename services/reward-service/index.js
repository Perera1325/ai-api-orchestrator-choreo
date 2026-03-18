const express = require("express");
const app = express();

app.get("/reward", (req, res) => {
    res.json({
        userId: "1",
        points: 120,
        reward: "10% discount"
    });
});

app.listen(3000, () => {
    console.log("Reward service running on port 3000");
});