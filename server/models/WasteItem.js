const mongoose = require('mongoose');

const WasteItemSchema = new mongoose.Schema({
  waste_id: { type: String, required: true, unique: true },
  date_listed: { type: Date, required: true },
  category: { type: String, required: true },
  sub_category: { type: String, required: true },
  description: { type: String },
  location: { type: String, required: true },
  quantity_kg: { type: Number, required: true },
  unit: { type: String, default: 'kg' },
  demand_index: { type: Number },     // AI Feature
  price_per_unit_lkr: { type: Number }, // Target Variable
  total_value_lkr: { type: Number },
  status: { type: String, enum: ['Available', 'Sold', 'Pending'], default: 'Available' }
});

module.exports = mongoose.model('WasteItem', WasteItemSchema);
