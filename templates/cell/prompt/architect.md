# System Instructions

## Request Received

This is a message we just received that needs to be acted upon.

#%- for field, value in message.items() %#
#% if '\n' in value %#
 * <{field}>:
<{value}>
#%- else %#
 * <{field}>: <{value}>
#%- endif %#
#%- endfor %#

## Tools Available

You may choose from the following tools to achieve your goals.

When executing a tool, reference the schema description and parameters
defined below and generate a JSON data object with the following structure:

```json
{
  "tool": "example:tool:name@local",
  "params": {
    "example_param1": "some value",
    "example_param2": "another value"
  }
}
````

It is important that only one tool is executed during each cycle so we can
more effectively preserve the history and encourage a more detailed dialog.
Always encapsulate the tool data in a Markdown ```json section with ending ```.

### Tool Reference

#%- for schema in tools %#
<{schema}>
#%- endfor %#
