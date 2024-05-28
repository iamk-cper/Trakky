import React, { useState } from "react";
import { View, TextInput, Button } from "react-native";
import axios from "axios";
import LoadingScreen from './LoadingScreen';
import { getUserData } from "../utils/Auth";

export function CustomDemand( {navigation} ) {
  const [isLoading, setIsLoading] = useState(false);
  const [userProfileData, setUserProfileData] = useState({
    fat: 0,
    carbs: 0,
    protein: 0
  });

  const handleChange = (key, val) => {
    setUserProfileData(prevState => ({ ...prevState, [key]: parseFloat(val) }));
  };

  const handleSubmit = async () => {
    setIsLoading(true);

    try {
      const { token } = await getUserData();
      const config = {
        headers: {
          'Authorization': 'Token ' + token
        }
      };

      const demandUrl = 'https://trakky.onrender.com/api/create_demand/';

      await axios.post(demandUrl, {
        fat : userProfileData.fat,
        protein : userProfileData.protein,
        carbohydrates : userProfileData.carbs,
        daily_calory_demand : userProfileData.fat * 9 + userProfileData.protein * 4 + userProfileData.carbs * 4

      }, config);
      console.log('Demand created successfully.');
      // Add further logic here for handling successful response
    } catch (error) {
      console.error('Error creating demand:', error);
      // Add further error handling logic here
    } finally {
      setIsLoading(false);
      navigation.reset({
        index: 0,
        routes: [{name: 'HomeScreen'}]
      });
    }
  };

  if (isLoading) {
    return <LoadingScreen />;
  }

  return (
    <View className="bg-gray-100 flex min-h-full flex-col px-6 py-12 lg:px-8">
      <View className="m-2">
        <TextInput
          placeholder="Enter Custom Fat Demand"
          keyboardType="numeric"
          onChangeText={(val) => handleChange("fat", val)}
        />
      </View>
      <View className="m-2">
        <TextInput
          placeholder="Enter Custom Carbs Demand"
          keyboardType="numeric"
          onChangeText={(val) => handleChange("carbs", val)}
        />
      </View>
      <View className="m-2">
        <TextInput
          placeholder="Enter Custom Protein Demand"
          keyboardType="numeric"
          onChangeText={(val) => handleChange("protein", val)}
        />
      </View>
      <View className="m-2">
        <Button 
          title="Submit"
          onPress={() => {
            handleSubmit()
          }}
        />
      </View>
    </View>
  );
}
