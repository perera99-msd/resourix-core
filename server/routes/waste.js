const express = require('express');
const router = express.Router();
const WasteItem = require('../models/WasteItem');

// @route   GET /api/waste
// @desc    Get all available waste items
// @access  Public
router.get('/', async (req, res) => {
  try {
    // Fetch items from MongoDB
    // .find({ status: 'Available' }) -> Only show unsold items
    // .sort({ date_listed: -1 })     -> Newest first
    // .limit(50)                     -> Don't crash the browser with 1000 items
    const items = await WasteItem.find({ status: 'Available' })
      .sort({ date_listed: -1 })
      .limit(50);

    res.json(items);
  } catch (err) {
    console.error(err.message);
    res.status(500).send('Server Error');
  }
});

module.exports = router;
