module.exports = {
  apps: [
    {
      name: "OPS_AWS_Cesar",
      script: "uvicorn main:app --host 127.0.0.1 --port 8001 --workers 4", 
      env: {
        PORT: 8001,
        ENVIRONMENT: "production",
      },
    },
  ],
};
