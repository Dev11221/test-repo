function calculateDiscount(price, discountPercent) {
  const discount = price * discountPercent / 100;
  return price - discount;
}

function formatReceipt(items) {
  let total = 0;

  for (const item of items) {
    total += calculateDiscount(item.price, item.discount || 0);
  }

  return {
    itemCount: items.length,
    total: total.toFixed(2),
  };
}

const cart = [
  { name: "Notebook", price: 12.5, discount: 10 },
  { name: "Pen", price: 2.75 },
];

console.log(formatReceipt(cart));
