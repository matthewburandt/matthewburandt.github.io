const express = require('express');
const cors = require('cors');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = 3001;
const CSV_FILE = path.join(__dirname, 'mailing_list.csv');

app.use(cors());
app.use(express.json());

// Ensure CSV file has headers
if (!fs.existsSync(CSV_FILE)) {
  fs.writeFileSync(CSV_FILE, 'Name,Email\n');
}

app.post('/api/subscribe', (req, res) => {
  const { name, email } = req.body;
  if (!name || !email) {
    return res.status(400).json({ success: false, message: 'Name and email are required.' });
  }
  // Basic email validation
  if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) {
    return res.status(400).json({ success: false, message: 'Invalid email address.' });
  }
  // Escape commas and newlines
  const safeName = String(name).replace(/,/g, ' ').replace(/\n/g, ' ');
  const safeEmail = String(email).replace(/,/g, ' ').replace(/\n/g, ' ');
  const line = `"${safeName}","${safeEmail}"\n`;
  fs.appendFile(CSV_FILE, line, err => {
    if (err) {
      return res.status(500).json({ success: false, message: 'Failed to save. Please try again.' });
    }
    res.json({ success: true, message: 'Thank you for subscribing!' });
  });
});

app.listen(PORT, () => {
  console.log(`Mailing list backend running on http://localhost:${PORT}`);
}); 