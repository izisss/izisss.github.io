var APP_DATA = {
  "scenes": [
    {
      "id": "0-couloir_d_bas",
      "name": "couloir_d_bas",
      "levels": [
        {
          "tileSize": 256,
          "size": 256,
          "fallbackOnly": true
        },
        {
          "tileSize": 512,
          "size": 512
        },
        {
          "tileSize": 512,
          "size": 1024
        },
        {
          "tileSize": 512,
          "size": 2048
        }
      ],
      "faceSize": 2048,
      "initialViewParameters": {
        "pitch": 0,
        "yaw": 0,
        "fov": 1.5707963267948966
      },
      "linkHotspots": [
        {
          "yaw": 2.492826416139433,
          "pitch": 0.06384153017767602,
          "rotation": 0,
          "target": "1-couloir_d"
        },
        {
          "yaw": -1.2452354857754244,
          "pitch": 0.08861443227644195,
          "rotation": 0,
          "target": "3-salle_"
        }
      ],
      "infoHotspots": []
    },
    {
      "id": "1-couloir_d",
      "name": "couloir_d",
      "levels": [
        {
          "tileSize": 256,
          "size": 256,
          "fallbackOnly": true
        },
        {
          "tileSize": 512,
          "size": 512
        },
        {
          "tileSize": 512,
          "size": 1024
        },
        {
          "tileSize": 512,
          "size": 2048
        }
      ],
      "faceSize": 2048,
      "initialViewParameters": {
        "pitch": 0,
        "yaw": 0,
        "fov": 1.5707963267948966
      },
      "linkHotspots": [
        {
          "yaw": -0.8599490156723828,
          "pitch": 0.26407074363129546,
          "rotation": 0,
          "target": "2-couloir_b"
        },
        {
          "yaw": -2.299741235698656,
          "pitch": -0.011765453203874898,
          "rotation": 0,
          "target": "0-couloir_d_bas"
        }
      ],
      "infoHotspots": []
    },
    {
      "id": "2-couloir_b",
      "name": "couloir_b",
      "levels": [
        {
          "tileSize": 256,
          "size": 256,
          "fallbackOnly": true
        },
        {
          "tileSize": 512,
          "size": 512
        },
        {
          "tileSize": 512,
          "size": 1024
        },
        {
          "tileSize": 512,
          "size": 2048
        }
      ],
      "faceSize": 2048,
      "initialViewParameters": {
        "yaw": -0.4177311266961219,
        "pitch": 0.32238093350619224,
        "fov": 1.1678810529903434
      },
      "linkHotspots": [
        {
          "yaw": -0.23088331636998305,
          "pitch": 0.23203377054092833,
          "rotation": 0,
          "target": "1-couloir_d"
        }
      ],
      "infoHotspots": []
    },
    {
      "id": "3-salle_",
      "name": "salle_",
      "levels": [
        {
          "tileSize": 256,
          "size": 256,
          "fallbackOnly": true
        },
        {
          "tileSize": 512,
          "size": 512
        },
        {
          "tileSize": 512,
          "size": 1024
        },
        {
          "tileSize": 512,
          "size": 2048
        }
      ],
      "faceSize": 2048,
      "initialViewParameters": {
        "pitch": 0,
        "yaw": 0,
        "fov": 1.5707963267948966
      },
      "linkHotspots": [
        {
          "yaw": -2.274804770219413,
          "pitch": 0.01013426923718086,
          "rotation": 0,
          "target": "0-couloir_d_bas"
        }
      ],
      "infoHotspots": []
    }
  ],
  "name": "Project Title",
  "settings": {
    "mouseViewMode": "drag",
    "autorotateEnabled": true,
    "fullscreenButton": false,
    "viewControlButtons": false
  }
};
