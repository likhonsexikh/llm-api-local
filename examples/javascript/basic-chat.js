import OpenAI from 'openai';
import 'dotenv/config'; // Load environment variables from .env file

// Configure for local model using environment variables
const openai = new OpenAI({
    baseURL: process.env.LOCAL_MODEL_BASE_URL || 'http://localhost:8080/v1',
    apiKey: process.env.LOCAL_API_KEY || 'dummy-key',
});

async function main() {
    try {
        // Use exactly like the OpenAI API
        const response = await openai.chat.completions.create({
            model: process.env.LOCAL_MODEL_NAME || 'ai/smollm2',
            messages: [
                { role: 'user', content: 'Hello! How are you?' },
            ],
        });

        console.log(response.choices[0].message.content);
    } catch (error) {
        console.error('Error communicating with the local model:', error);
    }
}

main();
