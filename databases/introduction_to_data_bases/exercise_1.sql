CREATE TABLE `products`(
    `id` INT NOT NULL,
    `code` TEXT NOT NULL,
    `name` TEXT NOT NULL,
    `price` DECIMAL(8, 2) NOT NULL,
    `entry_date` DATE NOT NULL,
    `brand` TEXT NOT NULL,
    `stock_available` INT NOT NULL,
    PRIMARY KEY(`id`)
);
ALTER TABLE
    `products` ADD UNIQUE `products_code_unique`(`code`);
CREATE TABLE `invoices`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `invoice_number` INT NOT NULL,
    `purchase_date` DATE NOT NULL,
    `buyer_email` TEXT NOT NULL,
    `total_amount` INT NOT NULL
);
ALTER TABLE
    `invoices` ADD UNIQUE `invoices_invoice_number_unique`(`invoice_number`);
CREATE TABLE `products_per_invoice`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `quantity` INT NOT NULL,
    `total_amount` INT NOT NULL
);
CREATE TABLE `shopping_cart`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `buyer_email` TEXT NOT NULL
);
CREATE TABLE `shopping_cart_product`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `shopping_cart_id` INT NOT NULL,
    `product_id` INT NOT NULL
);
ALTER TABLE
    `products` ADD CONSTRAINT `products_id_foreign` FOREIGN KEY(`id`) REFERENCES `shopping_cart_product`(`shopping_cart_id`);
ALTER TABLE
    `invoices` ADD CONSTRAINT `invoices_id_foreign` FOREIGN KEY(`id`) REFERENCES `products_per_invoice`(`id`);
ALTER TABLE
    `products` ADD CONSTRAINT `products_id_foreign` FOREIGN KEY(`id`) REFERENCES `products_per_invoice`(`id`);
ALTER TABLE
    `shopping_cart` ADD CONSTRAINT `shopping_cart_id_foreign` FOREIGN KEY(`id`) REFERENCES `shopping_cart_product`(`product_id`);