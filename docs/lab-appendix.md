# Lab Appendix:

### Appendix 1: Screen Pop – sample "index.php"

```php
<?php

// Check if the 'phone' parameter is set in the URL
if (isset($_GET['phone'])) {
    $phone = $_GET['phone'];

    // Dummy data mapping phone numbers to customer details
    $customerDirectory = [
        '6018' => [
            'name' => 'Charles Holland',
            'address' => '888 Oakland Street, RTP',
            'last_contacted' => '2025-05-25',
            'type' => 'VIP'
        ],
        '6016' => [
            'name' => 'Adam McKenzie',
            'address' => '123 Elm Street, Springfield',
            'last_contacted' => '2023-09-25',
            'type' => 'Regular'
        ],
        '6017' => [
            'name' => 'Anita Perez',
            'address' => '456 Oak Avenue, Springfield',
            'last_contacted' => '2023-10-02',
            'type' => 'VIP'
        ],
        '6099' => [
            'name' => 'Eric Steele',
            'address' => '789 Maple Lane, Springfield',
            'last_contacted' => '2023-09-15',
            'type' => 'New'
        ],
        '6050' => [
            'name' => 'Kellie Melby',
            'address' => '321 Birch Drive, Springfield',
            'last_contacted' => '2023-08-30',
            'type' => 'Regular'
        ],
        '6020' => [
            'name' => 'Monica Cheng',
            'address' => '654 Pine Court, Springfield',
            'last_contacted' => '2023-09-10',
            'type' => 'VIP'
        ],
        '6088' => [
            'name' => 'Rebekah Barretta',
            'address' => '987 Cedar Road, Springfield',
            'last_contacted' => '2023-09-20',
            'type' => 'New'
        ],
        '6083' => [
            'name' => 'Ricardo Filice',
            'address' => '111 Spruce Street, Springfield',
            'last_contacted' => '2023-10-01',
            'type' => 'Regular'
        ],
        '6072' => [
            'name' => 'Stefan Mauk',
            'address' => '222 Willow Boulevard, Springfield',
            'last_contacted' => '2023-09-22',
            'type' => 'VIP'
        ],
        '6026' => [
            'name' => 'Taylor Bard',
            'address' => '333 Aspen Circle, Springfield',
            'last_contacted' => '2023-09-18',
            'type' => 'New'
        ]
    ];

    // Check if the phone number exists in the dummy data
    if (isset($customerDirectory[$phone])) {
        $customer = $customerDirectory[$phone];

        // Display result as a styled table
        echo '<!DOCTYPE html>';
        echo '<html lang="en">';
        echo '<head>';
        echo '<meta charset="UTF-8">';
        echo '<meta name="viewport" content="width=device-width, initial-scale=1.0">';
        echo '<title>Customer Information</title>';
        echo '<style>';
        echo 'table { width: 50%; margin: 20px auto; border-collapse: collapse; }';
        echo 'th, td { padding: 10px; text-align: left; border: 1px solid #ddd; }';
        echo 'th { background-color: #f2f2f2; }';
        echo 'h2 { text-align: center; }';
        echo '</style>';
        echo '</head>';
        echo '<body>';
        echo '<h2>Customer Information</h2>';
        echo '<table>';
        echo '<tr><th>Name</th><th>Phone Number</th><th>Address</th><th>Last Contacted</th><th>Type of Customer</th></tr>';
        echo '<tr>';
        echo '<td>' . $customer['name'] . '</td>';
        echo '<td>' . $phone . '</td>';
        echo '<td>' . $customer['address'] . '</td>';
        echo '<td>' . $customer['last_contacted'] . '</td>';
        echo '<td>' . $customer['type'] . '</td>';
        echo '</tr>';
        echo '</table>';
        echo '</body>';
        echo '</html>';
    } else {
        echo 'Phone number not found.';
    }
} else {
    echo 'No phone number provided.';
}
?>
```

### Appendix 2: Related Sessions at WebexOne 2026

* CLS-11089: Level Up Your Customer Service: Webex Calling Customer Assist
* LAB-11169: Webex Calling Customer Assist Hands-On Lab
* CLS-21076: Webex Calling Customer Assist: Smarter Support, Made Simple

### Appendix 3: Online References

**Webex Calling AI Receptionist:**

* [https://help.webex.com/en-us/article/4chov0/AI-Receptionist-in-Webex-Calling](https://help.webex.com/en-us/article/4chov0/AI-Receptionist-in-Webex-Calling){:target="_blank" rel="noopener"}

**Webex Calling Customer Assist:**

* [https://help.webex.com/en-us/article/72sb3r/Webex-Calling-Customer-Assist](https://help.webex.com/en-us/article/72sb3r/Webex-Calling-Customer-Assist){:target="_blank" rel="noopener"}
* [https://help.webex.com/en-us/article/nc8142w/Get-started-with-Webex-Calling-Customer-Assist-for-Supervisors](https://help.webex.com/en-us/article/nc8142w/Get-started-with-Webex-Calling-Customer-Assist-for-Supervisors){:target="_blank" rel="noopener"}

