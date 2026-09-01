import React from 'react';
import {View, Text, StyleSheet} from 'react-native';

interface TitleProps {
  text: string;
  size: number;
}

const Title: React.FC<TitleProps> = ({text, size}) => {
  return (
    <View style={styles.container}>
      <Text style={{fontSize: size, color: '#333', fontWeight: 'bold'}}>
        {text}
      </Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    marginVertical: 10,
    alignItems: 'center',
  },
});

export default Title;