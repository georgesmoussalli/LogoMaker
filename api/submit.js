module.exports = async (req, res) => {
    const { text } = req.query;
    // Simulate API processing
    const response = { message: `Received: ${text}` };
    res.json(response);
  };
  