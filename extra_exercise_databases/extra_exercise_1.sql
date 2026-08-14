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
CREATE TABLE `users`(
    `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `full_name` TEXT NOT NULL,
    `email` TEXT NOT NULL,
    `registration_date` DATE NOT NULL
);
ALTER TABLE
    `users` ADD UNIQUE `users_email_unique`(`email`);
CREATE TABLE `reviews`(
    `review_id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `product_code` TEXT NOT NULL,
    `comment` TEXT NOT NULL,
    `rating` TINYINT NOT NULL,
    `date` DATE NOT NULL
);
ALTER TABLE
    `reviews` ADD UNIQUE `reviews_product_code_unique`(`product_code`);
CREATE TABLE `payment_method`(
    `method_id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `method_type` TEXT NOT NULL,
    `bank_name` TEXT NOT NULL
);
ALTER TABLE
    `users` ADD CONSTRAINT `users_id_foreign` FOREIGN KEY(`id`) REFERENCES `reviews`(`review_id`);
ALTER TABLE
    `users` ADD CONSTRAINT `users_id_foreign` FOREIGN KEY(`id`) REFERENCES `invoices`(`id`);
ALTER TABLE
    `products` ADD CONSTRAINT `products_id_foreign` FOREIGN KEY(`id`) REFERENCES `shopping_cart_product`(`shopping_cart_id`);
ALTER TABLE
    `invoices` ADD CONSTRAINT `invoices_id_foreign` FOREIGN KEY(`id`) REFERENCES `products_per_invoice`(`id`);
ALTER TABLE
    `products` ADD CONSTRAINT `products_id_foreign` FOREIGN KEY(`id`) REFERENCES `reviews`(`review_id`);
ALTER TABLE
    `products` ADD CONSTRAINT `products_id_foreign` FOREIGN KEY(`id`) REFERENCES `products_per_invoice`(`id`);
ALTER TABLE
    `shopping_cart` ADD CONSTRAINT `shopping_cart_id_foreign` FOREIGN KEY(`id`) REFERENCES `shopping_cart_product`(`product_id`);
ALTER TABLE
    `invoices` ADD CONSTRAINT `invoices_id_foreign` FOREIGN KEY(`id`) REFERENCES `payment_method`(`method_id`);