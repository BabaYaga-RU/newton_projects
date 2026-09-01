import React from 'react';
import {SafeAreaView, StyleSheet} from 'react-native';
import Title from './components/titulo';

const App = () => {
  return (
    <SafeAreaView style={styles.container}>
      <Title text="Bem-vindo!" size={24} />
      <Title text="Seu App React Native" size={18} />
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#f5f5f5',
  },
});

export default App;
