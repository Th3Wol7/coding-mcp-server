# MCP Server for AI-Assisted Code Generation

This MCP server enables an AI assistant to check the latest documentation of the libraries we are using before suggesting code. As a result, the generated code is always up to date. 

This server is designed to work seamlessly with **Claude Desktop** or **Claude Cloud**.

## Understanding Agentic Frameworks (My Explanation)

An **agent** is essentially a loop of calls to a language model that simulates a thought process—a **chain of thought**, really. When you send a query to an agentic framework, it initiates this loop to process the request.

The loop follows a structured pattern:
1. **Thought** – The model considers the problem.
2. **Action** – It selects an available function or API call based on its system prompt.
3. **Observation** – It executes the action and evaluates the result.

This cycle repeats, forming a continuous loop of reasoning and execution.

## Role of MCP Servers

An MCP server enhances this process by allowing the language model to use multiple toolkits or action calls across different APIs or functions—all following the same input-output protocol. This enables the model to **switch between tools sequentially**, making it capable of handling complex tasks efficiently.

### How MCP Servers Work

Each **MCP server** is treated as a **toolkit** that an AI model can use. These servers provide access to various functions that help complete user requests within specialized use cases. 

By integrating multiple MCP servers, the model gains the ability to:
- Perform a **wide range of specialized actions**.
- Improve **accuracy** in responses.
- Increase **real-world usefulness**.

This is made possible through the **MCP protocol**, which allows seamless connectivity between different MCP servers developed by various contributors.

### MCP Client/SDK

To ensure compatibility with the MCP protocol, when building I provide an **MCP client/SDK**. This enables connection to multiple MCP servers—each acting as a toolbox containing specialized tools and features that enhance the model’s capabilities.

With MCP servers, an AI model can gain access to:
- **Prompts**
- **Functions**
- **Resources**  
All of which help it complete tasks more effectively.

## About This MCP Server

This particular MCP server is designed with **one specialized tool**:  
A **library documentation search tool** that ensures Claude generates the most accurate and up-to-date code in a given programming language.

By integrating this server, I significantly **reduce the chances of outdated code** being generated, ensuring **reliable and current** AI-assisted coding.


## How to run in Claude Desktop

To run the server, you need to edit the Claude config by adding the following:

```json
"McpServers": {
    "documentation": {
        "command": "[Use 'pip' or 'uv']",
        "args": [
            "--directry",
            "[Path to working directory for your project]",
            "run",
            "main.py"
        ]
    }
}
```



## How to run in Claude Code

To add your project as an MCP (Managed Code Process) server in Claude Code, follow these steps:

1.  **Run the add command:**
    ```bash
    claude mcp add
    ```
    This command will open an interactive helper in your terminal.

2.  **Follow the interactive prompts:** The helper will guide you through adding the MCP server. You'll need to provide the following information:
    * **Name:** Give your MCP server a descriptive name.
    * **Project:** Enter the path to your project directory.
    * **Command:** Specify the command to use to run your project. This will likely be either `pip` or `uv`.
    * **Parameters:** For the parameters, enter the following, making sure to replace `[Insert full project directory location]` with the actual path to your project:
        ```
        --directory [Insert full project directory location]
        ```

3.  **Review and confirm:** Once you've entered all the details, the helper will likely show you a summary. Double-check that everything is correct and then press Enter to finish adding the MCP server.

4.  **List MCP servers:** To verify that your MCP server has been added successfully, run the following command:
    ```bash
    claude mpc list
    ```
    You should see your newly added MCP server listed in the output.

5.  **Test your MCP server:** After confirming it's listed, you can proceed to test your MCP server within Claude Code. The exact method for testing will depend on the functionality of your project and how Claude Code interacts with MCP servers.


How to debug the server.
To debug the server run npx @modelcontextprotocol/inspector pip run main.py
or npx @modelcontextprotocol/inspector uv run main.py 
Enter y to proceed then once the inspecter start running select the local host link to
inspect the server via the interface. The inspecter is a tool that allows you to debug your mcp server

## How to Debug the Server

To debug the server, run one of the following commands in your terminal:

```bash
npx @modelcontextprotocol/inspector python main.py
 ```
 or

```bash
npx @modelcontextprotocol/inspector uv run main.py
```

Enter `y` when prompted to proceed. Once the inspector starts running, select the provided localhost link to inspect the server through its web interface.

The inspector is a valuable tool that allows you to debug the MCP (Model Context Protocol) server effectively.


---

Feel free to contribute or extend this MCP server to support additional tools and functionalities!

I made this because of the problem of when using a coding assistant it doesn't have the latest version of the library your
using so to alleviate that, I built this.