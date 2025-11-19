import { Assistant } from "mastra";

export const {{ pattern.name }} = new Assistant({
  name: "{{ pattern.name }}",
  description: "Generated from Agentic AI Pattern KG",

  agents: [
    {% for agent in pattern.agents %}
    {
      name: "{{ agent }}",
      behavior: "default"
    }{% if not loop.last %},{% endif %}
    {% endfor %}
  ],

  tools: [
    {% for tool in pattern.tools %}
    "{{ tool }}"{% if not loop.last %},{% endif %}
    {% endfor %}
  ],

  workflow: [
    {% for step in pattern.steps %}
    {
      id: "{{ step.id }}",
      type: "{{ step.type }}",
      agent: "{{ step.agent }}",
      next: [
        {% for n in step.next %}
        "{{ n }}"{% if not loop.last %}, {% endif %}
        {% endfor %}
      ]
    }{% if not loop.last %},{% endif %}
    {% endfor %}
  ]
});