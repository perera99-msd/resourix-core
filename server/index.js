const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
require('dotenv').config();

const app = express();

// 1. Middleware
app.use(cors()); // Allow Frontend to talk to Backend
app.use(express.json());

// 2. Database Connection
mongoose.connect(process.env.MONGO_URI)
  .then(() => console.log('✅ MongoDB Connected'))
  .catch(err => console.log('❌ DB Connection Error:', err));

// 3. Routes
app.use('/api/waste', require('./routes/waste'));

// 4. Base Route (Health Check)
app.get('/', (req, res) => {
  res.send('API is running... Resourix Core Online.');
});

// 5. Start Server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`🚀 Server running on port ${PORT}`));
