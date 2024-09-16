const express = require('express');
const { exec } = require('child_process');

const app = express();

app.get('/run-scan', (req, res) => {
    exec('nmap -sP 192.168.1.1/24', (error, stdout, stderr) => {
        if (error) {
            return res.status(500).json({ error: stderr });
        }
        res.json({ result: stdout });
    });
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));