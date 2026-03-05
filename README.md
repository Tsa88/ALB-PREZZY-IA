# ALB-PREZZY-IA
Crie suas apresentações de forma simples, futurista e com os melhores templates e algoritimos.
{
  "final_presentation_structure": [
    { "id": "obj1", "type": "text", "content": "Título", "global_position": [0, 0], "global_scale": 1.0, "global_rotation": 0, "z_index": 1 },
    // ... outros objetos com suas propriedades globais
  ],
  "animation_plan": [
    {
      "transition_id": "trans_01",
      "start_path_point": { /* ... */ },
      "end_path_point": { /* ... */ },
      "frames": [
        { "timestamp": 0.0, "current_camera_state": [0, 0, 0.1, 0], "visible_objects": ["obj1", "frame1"], "narration_cue": "start" },
        { "timestamp": 0.05, "current_camera_state": [/* ... */], "visible_objects": [/* ... */] },
        // ... até o final da transição
        { "timestamp": 1.5, "current_camera_state": [/* ... */], "visible_objects": [/* ... */], "narration_cue": "end" }
      ]
    },
    // ... outras transições
  ]
}
