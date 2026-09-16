# Lab 4: Configure Webex Calling Customer Assist [20 minutes]

### Step 4.1: Create Customer Assist Queue

1. From Control Hub portal, under Services, click on “**Customer Assist**”.

2. Click on “**Queues**”

    ![](assets/docx-image-052.png)

3. Click “**Add queue**”

    ![](assets/docx-image-053.png)

4. Configure fields as below for “Basics” section:

    |  |  |
    | --- | --- |
    | **Location** | dCloud |
    | **Queue Name** | Customer Assist Queue |
    | **Phone number: Extension** | 6801 |
    | **Dial By name** | Customer Assist |
    | **External caller ID phone number** | Location Number |

    ![](assets/docx-image-054.png)

    Click “**Next**” to proceed to next section.

5. In Call Routing section, keep the default (Priority Based and Circular) selection. Click “Next” to continue.

    ![](assets/docx-image-055.png)

### Step 4.2: Configure Screen Pop

1. Click the toggle button to Configure Screen Pop.

    ![](assets/docx-image-056.png){ .bordered }

2. Click “**Add new**” in query parameters:

    ![](assets/docx-image-057.png){ .bordered }

3. Configure Screen pop as follow and then click “**Next**”

    |  |  |
    | --- | --- |
    | **Screen Pop URL** | http://crm.free.nf/index.php |
    | **Screen Pop Desktop Label** | Customer Assist CRM |
    | **Query Parameters: Key 1** | phone |
    | **Query Parameters: Value 1** | {{ "{{NewPhoneContact.ANI}}" }} |

    ![](assets/docx-image-058.png)

### Step 4.3: Configure Queue Announcements

1. In the Welcome Message section:

    * **Checked mark** on “Welcome message is mandatory”
    * Select “Custom Greeting” to use TTS Announcement created in Task 3.

2. Click “**Select File**” to use TTS Announcement file.

    ![](assets/docx-image-059.png)

3. Left Click on “**dCloud Customer Assist TTS**” and then click “**Select file**”

    ![](assets/docx-image-060.png){ width="753" }

    <div style="width:753px; text-align:center; font-size:2em; color:#1a73e8; line-height:1;">⬇</div>

    ![](assets/docx-image-061.png){ width="754" }

4. Enable “Comfort Message” and “Hold Music”. Then click “**Next**”.

    ![](assets/docx-image-062.png)

### Step 4.4: Select Agents

1. Add agents to Customer Assist Queue by selecting users from the “Search Users to add to queue” drop-down.

    ![](assets/docx-image-063.png){ width="960" }

2. Add “**Charles Holland**” and enabled “**Allow agents to join or unjoin the queue**”. Click “**Next**” when finished.

    ![](assets/docx-image-064.png){ width="960" }

3. Click “**Next**” to auto-assign Customer Assist license to Charles Holland.

    ![](assets/docx-image-065.png){ width="960" }

4. Finally click on “**Create**” to add this Customer Assist queue.

    ![](assets/docx-image-066.png){ width="960" }

5. Click “**Done**”

    ![](assets/docx-image-067.png){ width="960" }

6. List of Customer Assist Queue

    ![](assets/docx-image-068.png){ width="960" }

### Step 4.5: Set the Agents to “Join” state

Agent’s status is defaulted to **Unjoin** when created. Each Agent needs to join a queue or queues to be able to accept calls that arrive in the queues.

1. From Customer Assist section, click on “**Agent**”.

    ![](assets/docx-image-069.png){ width="960" }

2. Click on “**>**” as shown above to toggle agent’s status to “Join” by left click on “**Join**” button.

    ![](assets/docx-image-070.png){ width="960" }
